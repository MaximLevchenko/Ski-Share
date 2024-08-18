import React, { useEffect, useState } from 'react'

import s from './EditableCell.module.css'

const EditableCell = ({ cellData }) => {
  const [data, setData] = useState('')

  const handleData = (event) => {
    setData(event.target.value)
  }

  useEffect(() => {
    if (cellData) {
    }
  }, [cellData])

  return (
    <div>
      <div className={s.title}>Edit on {cellData}</div>
      <div>
        <input value={data} onChange={handleData} />
      </div>
    </div>
  )
}

export default EditableCell
