import { useRef, useState } from 'react'

import g from '../../App.module.css'
import Button from '../../components/Button/Button'
import OneDayCalendar from '../../components/OneDayCalendar/OneDayCalendar'
import { useOutsideClick } from '../../hooks/useOutSideClick'
import { useCreateClientMutation } from '../../store/apiSlices/clientApiSlice'
import s from './NewClient.module.css'
import { useNavigate } from 'react-router-dom'


const NewClient = () => {
  const navigate = useNavigate()
  const [createClient] = useCreateClientMutation()
  const [name, setName] = useState('')
  const [surname, setSurname] = useState('')
  const [email, setEmail] = useState('')
  const [phone, setPhone] = useState('')
  const [passportNumber, setPassportNumber] = useState('')
  const [address, setAddress] = useState('')
  const [birthDate, setBirthDate] = useState('')
  const [isOpenDatePicker, setIsOpenDatePicker] = useState(false)
  const [error, setError] = useState('')

  const datePickerRef = useRef()
  const dateInputRef = useRef()
  useOutsideClick(datePickerRef, () => setIsOpenDatePicker(false), dateInputRef)

  const handleSubmit = async (event) => {
    event.preventDefault()

    if (!name || !surname || !email || !phone || !passportNumber || !address || !birthDate) {
      setError('All fields are required!')
      return
    }

    if (!/^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email)) {
      setError('Invalid format of email.')
      return
    }

    if (!/^\+[1-9][0-9]{1,3}[0-9]+$/.test(phone)) {
      setError('Check again your phone number.')
      return
    }

    if (!/^[A-Za-z]{2}\d{6}$/.test(passportNumber)) {
      setError('You have incorrect passport number.')
      return
    }

    if (dateDifference() >= 0) {
      setError('Check again the birthday.')
      return
    }

    try {
      await createClient({
        name,
        surname,
        email,
        phone,
        passportNumber,
        address,
        birthDate: createDateString(),
      }).unwrap()
    } catch (e) {
    } finally {
      setName('')
      setSurname('')
      setEmail('')
      setPhone('')
      setPassportNumber('')
      setAddress('')
      setBirthDate('')
      setError('')
      navigate('/clients')
    }
  }

  function createDateString() {
    const actualDate = new Date(birthDate.y, birthDate.m - 1, birthDate.d)
    const year = actualDate.getFullYear()
    const month = String(actualDate.getMonth() + 1).padStart(2, '0')
    const day = String(actualDate.getDate()).padStart(2, '0')

    const dateString = `${year}-${month}-${day}`
    return dateString
  }

  function dateDifference() {
    const userTime = new Date()

    return (
      new Date(
        birthDate.y,
        birthDate.m - 1,
        birthDate.d,
        userTime.getHours(),
        userTime.getMinutes(),
        userTime.getSeconds()
      ).getTime() - userTime.getTime()
    )
  }

  return (
    <div className={g.initialPageContainer}>
      <div className={g.title}>New Client</div>
      <form onSubmit={handleSubmit}>
        <div className={s.formWrapper}>
          <div className={s.inputRow}>
            <input
              className={s.nameInput}
              type='text'
              placeholder='Petr'
              value={name}
              onChange={(event) => setName(event.target.value)}
              required
            />
            <input
              className={s.nameInput}
              type='text'
              placeholder='Pavel'
              value={surname}
              onChange={(event) => setSurname(event.target.value)}
              required
            />
          </div>
          <div className={s.inputRow}>
            <div className={s.datePicker}>
              <OneDayCalendar
                value={birthDate}
                setValue={setBirthDate}
                open={isOpenDatePicker}
                setOpen={setIsOpenDatePicker}
                dateInputRef={dateInputRef}
                ref={datePickerRef}
              />
            </div>
            <input
              type='tel'
              className={s.phoneInput}
              value={phone}
              onChange={(event) => setPhone(event.target.value)}
              placeholder='+420XXXXXXXX'
              required
            />
          </div>
          <div className={s.inputRow}>
            <input
              type='email'
              className={s.emailInput}
              placeholder='petr.pavel@gov.cz'
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              required
            />
          </div>
          <div className={s.inputRow}>
            <input
              className={s.nameInput}
              type='text'
              placeholder='Address'
              value={address}
              onChange={(event) => setAddress(event.target.value)}
              required
            />
            <input
              className={s.nameInput}
              type='text'
              placeholder='FV123567'
              value={passportNumber}
              onChange={(event) => setPassportNumber(event.target.value)}
              required
            />
          </div>
        </div>
        <div className={s.errorWrapper}>{error}</div>
        <div className={s.createButtonWrapper}>
          <Button>Create client</Button>
        </div>
      </form>
    </div>
  )
}

export default NewClient
