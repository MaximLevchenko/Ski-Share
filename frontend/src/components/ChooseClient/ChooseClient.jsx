import { useState } from 'react'
import { AiOutlineCheck, AiOutlinePlus } from 'react-icons/ai'

import search from '../../res/icons/search.svg'
import { useFetchClientsQuery } from '../../store/apiSlices/clientApiSlice'
import SkeletonList from '../Loaders/SkeletonList'
import s from './ChooseClient.module.css'


const ChooseClient = ({ handleChooseClient, choosenClient }) => {
  const { data, error, isLoading } = useFetchClientsQuery()
  const [searchTerm, setSearchTerm] = useState('')

  let content
  if (isLoading) {
    content = <SkeletonList />
  } else if (error) {
    content = <div>Error with fetching users</div>
  } else {
    const filteredUsers = data.filter(
      (user) =>
        user.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        user.surname.toLowerCase().includes(searchTerm.toLowerCase())
    )
    content = filteredUsers.map((user) => (
      <ClientItem
        key={user.id}
        handleChooseClient={handleChooseClient}
        name={`${user.name} ${user.surname}`}
        passportNumber={user.passport_number}
        user={user}
        choosenClient={choosenClient}
      />
    ))
  }

  const handleSearchTerm = (event) => {
    setSearchTerm(event.target.value)
  }

  return (
    <div>
      <div className={s.inputWrapper}>
        <img src={search} alt='Search' />
        <input type='text' placeholder='Search' onChange={handleSearchTerm} />
      </div>
      <div className={s.clientsWrapper}>{content}</div>
    </div>
  )
}

const ClientItem = ({ name, passportNumber, user, handleChooseClient, choosenClient }) => {
  const renderedIcon =
    choosenClient?.id === user.id ? (
      <AiOutlineCheck size={25} className={s.choosenIcon} onClick={() => handleChooseClient(user)} />
    ) : (
      <AiOutlinePlus size={25} className={s.icon} onClick={() => handleChooseClient(user)} />
    )

  return (
    <div className={s.clientItem}>
      {renderedIcon}
      <div className={s.name}>{name}</div>
      <div>{passportNumber}</div>
    </div>
  )
}

export default ChooseClient
