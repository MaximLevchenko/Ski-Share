import { useState } from 'react'
import { BsArrowDown, BsArrowDownUp, BsArrowUp } from 'react-icons/bs'

import Table from '../Table/Table'
import s from './SortableTable.module.css'


const SortableTable = (props) => {
  const [sortOrder, setSortOrder] = useState(null)
  const [sortBy, setSortBy] = useState(null)

  const { config, data } = props

  const handleClick = (label) => {
    if (sortBy && label !== sortBy) {
      setSortOrder('asc')
      setSortBy(label)
      return
    }

    if (sortOrder === null) {
      setSortOrder('asc')
      setSortBy(label)
    } else if (sortOrder === 'asc') {
      setSortOrder('desc')
      setSortBy(label)
    } else if (sortOrder === 'desc') {
      setSortOrder(null)
      setSortBy(null)
    }
  }

  const updatedConfig = config.map((column) => {
    if (!column.sortValue) {
      return column
    }

    return {
      ...column,
      header: () => (
        <th className={s.header} onClick={() => handleClick(column.label)}>
          <div className={s.cell}>
            {getIcons(column.label, sortBy, sortOrder)}
            {column.label}
          </div>
        </th>
      ),
    }
  })

  let sortedData = data

  if (sortOrder && sortBy) {
    const { sortValue } = config.find((column) => column.label === sortBy)
    sortedData = [...data].sort((a, b) => {
      const valueA = sortValue(a)
      const valueB = sortValue(b)

      const reverseOrder = sortOrder === 'asc' ? 1 : -1

      if (typeof valueA === 'string') {
        return valueA.localeCompare(valueB) * reverseOrder
      } else {
        return (valueA - valueB) * reverseOrder
      }
    })
  }

  return (
    <div>
      <Table {...props} data={sortedData} config={updatedConfig} />
    </div>
  )
}

function getIcons(label, sortBy, sortOrder) {
  if (label !== sortBy) {
    return (
      <div className={s.filterIcons}>
        <BsArrowDownUp size={20} />
      </div>
    )
  }

  if (sortOrder === null) {
    return (
      <div className={s.filterIcons}>
        <BsArrowDownUp size={20} />
      </div>
    )
  } else if (sortOrder === 'asc') {
    return (
      <div>
        <BsArrowUp size={20} />
      </div>
    )
  } else if (sortOrder === 'desc') {
    return (
      <div>
        <BsArrowDown size={20} />
      </div>
    )
  }
}

export default SortableTable
