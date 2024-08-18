import { useState } from 'react'
import { Link } from 'react-router-dom'

import s from './Dropdown.module.css'


const Dropdown = ({ children, dropdownMenu }) => {
  const [isOpen, setIsOpen] = useState(false)

  const handleOpen = () => {
    setIsOpen(!isOpen)
  }

  const renderedMenu = dropdownMenu.map((item) => (
    <div key={item.navigate}>
      <Link to={item.navigate}>
        {item.title}
      </Link>
    </div>
  ))

  return (
    <>
      <button className={s.Dropdown} onClick={handleOpen}>
        {children}
      </button>
      {isOpen && <div className={s.dropdownMenu} onClick={() => setIsOpen(false)}>{renderedMenu}</div>}
    </>
  )
}

export default Dropdown
