import { useEffect, useRef, useState } from 'react'
import { AiOutlinePlus } from 'react-icons/ai'
import { ImCancelCircle } from 'react-icons/im'
import { useSelector } from 'react-redux'
import { useNavigate } from 'react-router-dom'

import g from '../../App.module.css'
import Button from '../../components/Button/Button'
import ChooseClient from '../../components/ChooseClient/ChooseClient'
import ChooseEquipment from '../../components/ChooseEquipment/ChooseEquipment'
import Modal from '../../components/Modal/Modal'
import OneDayCalendar from '../../components/OneDayCalendar/OneDayCalendar'
import { useOutsideClick } from '../../hooks/useOutSideClick'
import { useCreateNewRentalMutation } from '../../store/apiSlices/rentalApiSlice'
import s from './NewRent.module.css'

const NewRent = () => {
  const navigate = useNavigate()
  const user = useSelector((state) => state.auth.user)
  const [createRental] = useCreateNewRentalMutation()

  const [choosenTime, setChoosenTime] = useState(null)
  const [choosenTimeError, setChoosenTimeError] = useState('')

  // Calendar
  const [open, setOpen] = useState(false)

  // Clients modal
  const [isOpenModalClient, setIsOpenModalClient] = useState(false)
  const [choosenClient, setChoosenClient] = useState(null)
  const [clientError, setClientError] = useState('')

  // Equipment modal
  const [isOpenModalEquipment, setIsOpenModalEquipment] = useState(false)
  const [choosenEquipment, setChoosenEquipment] = useState([])
  const [equipmentError, setEquipmentError] = useState('')

  // Rental stats
  const [rentalTime, setRentalTime] = useState(null)
  const [priceToPay, setPriceToPay] = useState(null)

  const [generalError, setGeneralError] = useState('')

  useEffect(() => {
    if (choosenTime && new Date(choosenTime.y, choosenTime.m - 1, choosenTime.d) < new Date()) {
      setChoosenTimeError('Your date must be greater than the current date.')
      setChoosenTime(null)
      setRentalTime(null)
    } else if (choosenTime) {
      setRentalTime(getHoursDifferenceFromNow())
      setChoosenTimeError('')
    }
  }, [choosenTime])

  useEffect(() => {
    if (!choosenTime) {
      setRentalTime(null)
    }
    if (!choosenEquipment.length) {
      setPriceToPay(null)
    }
  }, [choosenTime, choosenEquipment.length])

  useEffect(() => {
    if (choosenEquipment.length && rentalTime) {
      let sum = 0
      choosenEquipment.forEach((equipment) => (sum += equipment.price_per_hour))
      setPriceToPay(sum * rentalTime)
    }
  }, [choosenEquipment.length, rentalTime])

  const datePickerRef = useRef()
  const dateInputRef = useRef()
  useOutsideClick(datePickerRef, () => setOpen(false), dateInputRef)

  const handleChooseClientModal = () => {
    setIsOpenModalClient(!isOpenModalClient)
  }

  const handleChooseClient = (user) => {
    setChoosenClient(user)
    setIsOpenModalClient(false)
    setClientError('') // Clear error when client is chosen
  }

  const handleDeleteUser = () => {
    setChoosenClient(null)
  }

  const handleChooseEquipmentModal = () => {
    setIsOpenModalEquipment(!isOpenModalEquipment)
  }

  const handleChooseEquipment = (equipment) => {
    const index = choosenEquipment.findIndex(
      (inventoryNumber) => inventoryNumber.inventory_number === equipment.inventory_number
    )
    if (index === -1) {
      setChoosenEquipment((state) => [...state, equipment])
      setEquipmentError('') // Clear error when equipment is chosen
    } else {
      setChoosenEquipment(choosenEquipment.filter((item) => item.inventory_number !== equipment.inventory_number))
    }
  }

  const handleSaveRent = async () => {
    let hasError = false

    // Ensure required fields are populated and set errors if not
    if (!choosenTime) {
      setGeneralError('Please choose a rental time.')
      hasError = true
    }
    if (!choosenClient) {
      setClientError('Please choose a client.')
      hasError = true
    }
    if (!choosenEquipment.length) {
      setEquipmentError('Please choose at least one piece of equipment.')
      hasError = true
    }

    if (hasError) {
      return
    }

    const res = {
      dateEnd: createDateString(),
      paymentType: 'Card',
      basePrice: priceToPay || 0, // Ensure priceToPay is defined, default to 0 if not
      employeeId: user.employeeId, // Make sure user and employeeId are defined
      clientId: choosenClient.id, // Ensure client ID is available
      equipments: choosenEquipment.map((equipment) => equipment.inventory_number), // Ensure equipment is properly mapped
    }

    try {
      await createRental(res).unwrap()
      // Reset the form after successful submission
      setChoosenTime(null)
      setChoosenTimeError('')
      setIsOpenModalClient(false)
      setChoosenClient(null)
      setIsOpenModalEquipment(false)
      setChoosenEquipment([])
      setRentalTime(null)
      setPriceToPay(null)
      navigate('/rents')
    } catch (err) {
      setGeneralError('Failed to create rental. Please try again.')
      console.error('Failed to create rental:', err)
    }
  }

  const clientsModal = (
    <Modal onClose={() => setIsOpenModalClient(false)}>
      <ChooseClient handleChooseClient={handleChooseClient} choosenClient={choosenClient} />
    </Modal>
  )

  const equipmentModal = (
    <Modal onClose={() => handleChooseEquipmentModal(false)}>
      <ChooseEquipment
        choosenEquipment={choosenEquipment}
        setChoosenEquipment={setChoosenEquipment}
        handleChooseEquipment={handleChooseEquipment}
      />
    </Modal>
  )

  function createDateString() {
    const actualDate = new Date(choosenTime.y, choosenTime.m - 1, choosenTime.d)
    const year = actualDate.getFullYear()
    const month = String(actualDate.getMonth() + 1).padStart(2, '0')
    const day = String(actualDate.getDate()).padStart(2, '0')

    const dateString = `${year}-${month}-${day}T20:00:00.000Z`
    return dateString
  }

  function getHoursDifferenceFromNow() {
    const currentDate = new Date()
    const currentEndDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDay(), 20, 0, 0)
    const targetDate = new Date(choosenTime.y, choosenTime.m - 1, choosenTime.d, 20, 0, 0)
    const differenceInHoursToday = Math.floor(Math.abs(currentEndDate - currentDate) / (1000 * 60 * 60))
    const differenceInDays = Math.floor(Math.abs(targetDate - currentEndDate) / (1000 * 60 * 60 * 24))
    return differenceInHoursToday + differenceInDays * 12
  }

  const isSaveEnabled = choosenTime && choosenClient && choosenEquipment.length > 0

  return (
    <div className={g.initialPageContainer}>
      <div className={g.title}>New Rent</div>
      <div className={s.rentContainer}>
        <div className={s.subtitle}>Rent time</div>
        <div className={s.container}>
          <div className={s.inputsContainer}>
            <div>
              <div className={s.datePicker}>
                <OneDayCalendar
                  value={choosenTime}
                  setValue={setChoosenTime}
                  open={open}
                  setOpen={setOpen}
                  dateInputRef={dateInputRef}
                  setPriceToPay={setPriceToPay}
                  ref={datePickerRef}
                />
              </div>
              <div className={s.timeError}>{choosenTimeError}</div>
            </div>
            <div className={s.chooseClientWrapper}>
              <div className={s.subtitle}>Choose client</div>
              <div className={s.buttonContainer}>
                <Button onClick={handleChooseClientModal}>
                  <AiOutlinePlus size={25} /> New client
                </Button>
                {isOpenModalClient && clientsModal}
              </div>
              {clientError && <div className={s.timeError}>{clientError}</div>}
            </div>
            {choosenClient && <ViewUser user={choosenClient} onClick={handleDeleteUser} />}
            <div className={s.chooseClientWrapper}>
              <div className={s.subtitle}>Choose </div>
              <div className={s.buttonContainer}>
                <Button onClick={handleChooseEquipmentModal}>
                  <AiOutlinePlus size={25} /> Equipment
                </Button>
                {isOpenModalEquipment && equipmentModal}
              </div>
              {equipmentError && <div className={s.timeError}>{equipmentError}</div>}
            </div>
            {!!choosenEquipment.length && (
              <ViewEquipment equipment={choosenEquipment} onClick={handleChooseEquipment} />
            )}
          </div>
          <div className={s.statsContainer}>
            <div className={s.statsBlock}>
              <div className={s.statsTitle}>Total</div>
              <div className={s.statsInfo}>Rental time - {choosenTime && <>{rentalTime}h</>}</div>
              <div className={s.statsInfo}>TO PAY - {priceToPay && <>${priceToPay}</>}</div>
            </div>
            <div className={s.saveButtonWrapper}>
              <Button onClick={handleSaveRent} disabled={!isSaveEnabled}>
                Save rent
              </Button>
              {generalError && <div className={s.timeError}>{generalError}</div>}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

function ViewUser({ user, onClick }) {
  return (
    <div className={s.viewBlock}>
      <div className={s.itemRow}>
        {user.name} {user.surname}
        <ImCancelCircle size={25} style={{ color: 'red', cursor: 'pointer' }} onClick={onClick} />{' '}
      </div>
    </div>
  )
}

function ViewEquipment({ equipment, onClick }) {
  const renderedEquipment = equipment.map((item) => (
    <div className={s.itemRow} key={item.inventory_number}>
      <div>
        {item.manufacturer} {item.model}
      </div>
      <div>
        <ImCancelCircle size={25} style={{ color: 'red', cursor: 'pointer' }} onClick={() => onClick(item)} />{' '}
      </div>
    </div>
  ))

  return <div className={s.viewBlock}>{renderedEquipment}</div>
}

export default NewRent
