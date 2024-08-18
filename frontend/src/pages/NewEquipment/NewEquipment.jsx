import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'

import g from '../../App.module.css'
import Button from '../../components/Button/Button'
import Select from '../../components/Select/Select'
import { useCreateEquipmentMutation } from '../../store/apiSlices/equipmentApiSlice'
import s from './NewEquipment.module.css'


const NewEquipment = () => {
  const navigate = useNavigate()
  const [createEquipment, results] = useCreateEquipmentMutation()
  const [model, setModel] = useState('')
  const [manufacturer, setManufacturer] = useState('')
  const [category, setCategory] = useState(null)
  const [size, setSize] = useState('')
  const [pricePerHour, setPricePerHour] = useState('')
  const [description, setDescription] = useState('')
  const [error, setError] = useState('')

  useEffect(() => {
    setError('')
  }, [model, manufacturer, category, pricePerHour, description])

  const handleSelect = (option) => {
    setCategory(option)
  }

  const handleChangePrice = (event) => {
    const value = parseInt(event.target.value) || 0
    setPricePerHour(value)
  }

  const handleSubmit = async (event) => {
    event.preventDefault()

    if (!model || !manufacturer || !category || !description || !size) {
      setError('All fields are required.')
      return
    }

    if (pricePerHour <= 0) {
      setError('Price per hour is required and must be a positive number.')
      return
    }

    try {
      const data = await createEquipment({
        category: category.value,
        manufacturer,
        model,
        pricePerHour,
        description,
        size
      }).unwrap()
    } catch (e) {
      console.log(e)
    } finally {
      setModel('')
      setManufacturer('')
      setCategory(null)
      setSize('')
      setPricePerHour('')
      setDescription('')
      setError('')
      navigate('/equipment')
    }
  }

  const options = [
    { label: 'Ski', value: 'Ski' },
    { label: 'Snowboard', value: 'Snowboard' },
    { label: 'Ski boots', value: 'Ski boots' },
    { label: 'Snowboard boots', value: 'Snowboard boots' },
    { label: 'Helmet', value: 'Helmet' },
    { label: 'Ski poles', value: 'Ski poles' },
    { label: 'Ski suit', value: 'Ski suit' },
  ]

  return (
    <div className={g.initialPageContainer}>
      <form onSubmit={handleSubmit}>
        <div className={g.title}>New equipment</div>
        <div className={s.formWrapper}>
          <div className={s.inputRow}>
            <input
              className={s.nameInput}
              type='text'
              placeholder='Sender 94 Ti Skis 2023'
              value={model}
              onChange={(event) => setModel(event.target.value)}
              required
            />
            <input
              className={s.nameInput}
              type='text'
              placeholder='Brand'
              value={manufacturer}
              onChange={(event) => setManufacturer(event.target.value)}
              required
            />
            <input
              className={s.nameInput}
              type='text'
              placeholder='Size'
              value={size}
              onChange={(event) => setSize(event.target.value)}
              required
            />
          </div>
          <div className={s.inputRow}>
            <div className={s.selectWrapper}>
              <Select category={category} onChange={handleSelect} options={options} />
            </div>
            <input
              className={s.nameInput}
              type='number'
              placeholder='Price per hour'
              value={pricePerHour || ''}
              onChange={handleChangePrice}
              required
            />
          </div>
          <div className={s.inputRow}>
            <textarea
              className={s.descriptionInput}
              type='text'
              placeholder='Description...'
              value={description}
              onChange={(event) => setDescription(event.target.value)}
              required
            />
          </div>
        </div>
        <div className={s.errorWrapper}>{error}</div>
        <div className={s.createButtonWrapper}>
          <Button>Create equipment</Button>
        </div>
      </form>
    </div>
  )
}

export default NewEquipment
