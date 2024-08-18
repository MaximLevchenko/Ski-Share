import { useState } from 'react'

import g from '../../App.module.css'
import SkeletonBlock from '../../components/Loaders/SkeletonBlock'
import SortableTable from '../../components/SortableTable/SortableTable'
import search from '../../res/icons/search.svg'
import { useFetchClientsQuery } from '../../store/apiSlices/clientApiSlice'
import s from './Clients.module.css'


const Clients = () => {
  const { data, error, isLoading } = useFetchClientsQuery()
  const [searchTerm, setSearchTerm] = useState('')

  const handleSearchTerm = (event) => {
    setSearchTerm(event.target.value)
  }

  let config = [
    {
      label: 'Name',
      render: (client) => client.name,
      sortValue: (client) => client.name,
    },
    {
      label: 'Surname',
      render: (client) => client.surname,
      sortValue: (client) => client.surname,
    },
    {
      label: 'Email',
      render: (client) => client.email,
      sortValue: (client) => client.email,
    },
    {
      label: 'Phone',
      render: (client) => client.phone,
      sortValue: (client) => client.phone,
    },
    {
      label: 'Address',
      render: (client) => client.address,
      sortValue: (client) => client.address,
    },
    {
      label: 'Passport number',
      render: (client) => client.passport_number,
      sortValue: (client) => client.passport_number,
    },
    {
      label: 'Birthday',
      render: (client) => client.birth_date,
      sortValue: (client) => client.birth_date,
    },
  ]

  let content

  if (isLoading) {
    content = <SkeletonBlock />
  } else if (error) {
    content = <div>Some error with table</div>
  } else {
    const newData = data?.filter(
      (user) =>
        user.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        user.surname.toLowerCase().includes(searchTerm.toLowerCase())
    )
    content = <SortableTable data={newData} config={config} keyFn={keyFn} />
  }

  return (
    <div className={g.initialPageContainer}>
      <div className={g.title}>Clients</div>
      <div className={s.clientsWrapper}>
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

export default Clients
