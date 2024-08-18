import { useEffect, useRef, useState } from 'react'

import { MdOutlineKeyboardArrowDown, MdOutlineKeyboardArrowRight } from 'react-icons/md'
import s from './Select.module.css'


const Select = ({ category, onChange, options }) => {
  const [isOpen, setIsOpen] = useState(false)
  const divEl = useRef()

  useEffect(() => {
    const handler = (event) => {
      if (!divEl.current) {
        return
      }

      if (!divEl.current.contains(event.target)) {
        setIsOpen(false)
      }
    }

    document.addEventListener('click', handler, true)

    return () => {
      document.removeEventListener('click', handler)
    }
  }, [])

  const handleClick = () => {
    setIsOpen(!isOpen)
  }

  const handleOptionClick = (option) => {
    setIsOpen(false)
    onChange(option)
  }

  const renderedOptions = options.map((option) => (
    <div className={s.option} onClick={() => handleOptionClick(option)} key={option.value}>
      {option.label}
    </div>
  ))

  return (
    <div ref={divEl} className={s.selectItem} onClick={handleClick}>
      <div className={s.Select}>
        {!isOpen ? <MdOutlineKeyboardArrowDown size={25} /> : <MdOutlineKeyboardArrowRight size={25} />}
        {category?.label || '-'}
      </div>
      {isOpen && <div className={s.options}>{renderedOptions}</div>}
    </div>
  )
}

export default Select
