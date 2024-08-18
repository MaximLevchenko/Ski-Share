import { useState } from "react"
import g from '../../App.module.css'
import SkeletonBlock from "../../components/Loaders/SkeletonBlock"
import SortableTable from "../../components/SortableTable/SortableTable"
import search from '../../res/icons/search.svg'
import { useFetchRentalsQuery } from "../../store/apiSlices/rentalApiSlice"
import s from './Rents.module.css'


const Rents = () => {
  const {data, error, isLoading} = useFetchRentalsQuery()
  const [searchTerm, setSearchTerm] = useState('')

  const handleSearchTerm = (event) => {
    setSearchTerm(event.target.value)
  }

  let config = [
    {
      label: 'Date start',
      render: (rent) => rent.date_start,
      sortValue: (rent) => rent.date_start,
    },
    {
      label: 'Date end',
      render: (rent) => rent.date_end,
      sortValue: (rent) => rent.date_end,
    },
  ]

  let content

  if (isLoading) {
    content = <SkeletonBlock />
  } else if (error) {
    content = <div>Some error with table</div>
  } else {
    const newData = data?.filter(
      (rent) =>
      rent.date_start.toLowerCase().includes(searchTerm.toLowerCase()) ||
      rent.date_end.toLowerCase().includes(searchTerm.toLowerCase())
    )
    content = <SortableTable data={newData} config={config} keyFn={keyFn} />
  }

  return (
    <div className={g.initialPageContainer}>
      <div className={g.title}>Rents</div>
      <div className={s.rentsWrapper}>
        <div className={s.inputWrapper}>
          <img src={search} alt='Search' />
          <input type='text' placeholder='Search' value={searchTerm} onChange={handleSearchTerm} />
        </div>
        <div className={s.tableWrapper}>{content}</div>
      </div>
    </div>
  )
}

const keyFn = (client) => {
  return client.id
}

export default Rents