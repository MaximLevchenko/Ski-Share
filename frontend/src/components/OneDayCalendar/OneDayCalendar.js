import { forwardRef, useState } from 'react'

import s from './Calendars.module.css'
import { useDate } from './getMonth'


export default forwardRef(function OneDayCalendar({ value, setValue, open, setOpen, dateInputRef, setPriceToPay }, ref) {
  const { getMonthArr } = useDate()
  const [currentDate, setCurrentDate] = useState(new Date())
  const [arr, setArr] = useState(getMonthArr(new Date()))

  const clickHandler = (day) => {
    if (day === value) {
      setValue(null)
      setPriceToPay && setPriceToPay(null)
    } else {
      if (day.d !== 0) {
        setValue(day)
        setOpen(2)
      }
    }
  }

  const getStyle = (day) => {
    if (day.d === 0) {
      return s.noDay
    }
    if (value) {
      if (day.d === value.d && day.m === value.m && day.y === value.y) {
        return s.daySelected
      }
    }

    return s.day
  }

  const Weeks = arr.map((week, index) => {
    return (
      <tr key={index}>
        {week.map((day, dayIndex) => {
          return (
            <td key={`${index}-${dayIndex}`} className={getStyle(day)} onClick={() => clickHandler(day)}>
              {day.d ? day.d : ''}
            </td>
          )
        })}
      </tr>
    )
  })

  const getCurrentDate = (date) => {
    let m
    switch (date.getMonth()) {
      case 0:
        m = 'January'
        break
      case 1:
        m = 'February'
        break
      case 2:
        m = 'March'
        break
      case 3:
        m = 'April'
        break
      case 4:
        m = 'May'
        break
      case 5:
        m = 'June'
        break
      case 6:
        m = 'July'
        break
      case 7:
        m = 'August'
        break
      case 8:
        m = 'September'
        break
      case 9:
        m = 'October'
        break
      case 10:
        m = 'November'
        break
      case 11:
        m = 'December'
        break
    }
    return `${m}, ${date.getFullYear()}`
  }

  const nextMoth = () => {
    let newDate
    if (currentDate.getMonth() === 11) {
      newDate = new Date(currentDate.getFullYear() + 1, 0, 1)
    } else {
      newDate = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1)
    }
    setCurrentDate(newDate)
    setArr(getMonthArr(newDate))
  }

  const prevMonth = () => {
    let newDate
    if (currentDate.getMonth() === 0) {
      newDate = new Date(currentDate.getFullYear() - 1, 11, 1)
    } else {
      newDate = new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1)
    }
    setCurrentDate(newDate)
    setArr(getMonthArr(newDate))
  }


  return (
    <div className={s.container}>
      <div
        ref={dateInputRef}
        className={s.input}
        onClick={() => {
          setOpen(true)
        }}
      >
        {value ? `${value.d}.${value.m}.${value.y}` : 'choose date'}
      </div>
      {open ? (
        <div
          className={open === 2 ? s.calendarHide : s.calendar}
          onAnimationEnd={() => {
            if (open === 2) {
              setOpen(false)
            }
          }}
          ref={ref}
        >
          <div className={s.head}>
            <div className={s.arrowContainer} onClick={prevMonth}>
              <div className={s.arrowPrev}></div>
            </div>
            <div className={s.month}>{getCurrentDate(currentDate)}</div>
            <div className={s.arrowContainer} onClick={nextMoth}>
              <div className={s.arrowNext}></div>
            </div>
          </div>
          <table className={s.table}>
            <thead>
              <tr>
                <th>mon</th>
                <th>tue</th>
                <th>wed</th>
                <th>thu</th>
                <th>fri</th>
                <th>sat</th>
                <th>sun</th>
              </tr>
            </thead>
            <tbody>{Weeks}</tbody>
          </table>
        </div>
      ) : null}
    </div>
  )
})
