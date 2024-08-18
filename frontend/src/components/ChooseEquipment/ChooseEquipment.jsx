import { useState } from 'react'
import classNames from 'classnames'

import search from '../../res/icons/search.svg'
import { useFetchEquipmentsQuery } from '../../store/apiSlices/equipmentApiSlice'
import SkeletonList from '../Loaders/SkeletonList'
import s from './ChooseEquipment.module.css'


const ChooseEquipment = ({ choosenEquipment, setChoosenEquipment, handleChooseEquipment }) => {
  const { data, error, isLoading } = useFetchEquipmentsQuery()
  const [searchTerm, setSearchTerm] = useState('')
  const [priceInputFirst, setPriceInputFirst] = useState('')
  const [priceInputSecond, setPriceInputSecond] = useState('')

  const handlePriceInputFirst = (event) => {
    setPriceInputFirst(event.target.value)
  }

  const handlePriceInputSecond = (event) => {
    setPriceInputSecond(event.target.value)
  }

  const handleSearchTerm = (event) => {
    setSearchTerm(event.target.value)
  }



  let content
  if (isLoading) {
    content = <SkeletonList />
  } else if (error) {
    content = <div>Error fetching equipment</div>
  } else {
    const filteredEquipments = data.filter(
      (equipment) =>
        equipment.manufacturer.toLowerCase().includes(searchTerm.toLowerCase()) ||
        equipment.model.toLowerCase().includes(searchTerm.toLowerCase())
    )

    content = filteredEquipments.map((equipment) => {
      return (
        <EquipmentItem
          key={equipment.inventory_number}
          choosenEquipment={choosenEquipment}
          equipment={equipment}
          onClick={handleChooseEquipment}
        />
      )
    })
  }

  return (
    <div>
      <div className={s.title}>Choose Equipment</div>
      <div className={s.subtitle}>Total: {choosenEquipment.length}</div>
      <div className={s.searchBar}>
        <div className={s.inputWrapper}>
          <img src={search} alt='Search' />
          <input type='text' value={searchTerm} placeholder='Search' onChange={handleSearchTerm} />
        </div>
      </div>
      <div className={s.equipmentWrapper}>
        <div className={s.filters}>
          <div className={s.filterColumn}>
            <div className={s.filterTitle}>Filter</div>
            <div className={s.filterSubtitle}>Price</div>
            <div className={s.section}>
              <div className={s.filterInputWrapper}>
                <div className={s.filterInput}>
                  <input type='text' value={priceInputFirst} onChange={handlePriceInputFirst} />
                </div>
                <div className={s.filterTab}>&#8211;</div>
                <div className={s.filterInput}>
                  <input type='text' value={priceInputSecond} onChange={handlePriceInputSecond} />
                </div>
              </div>
            </div>
            <div className={s.section}>
              <div className={s.filterSubtitle}>Brands</div>
            </div>
            <div className={s.section}>
              <div className={s.filterSubtitle}>Equipment</div>
            </div>
          </div>
        </div>
        <div className={s.marketPlace}>{content}</div>
      </div>
    </div>
  )
}

const EquipmentItem = ({ equipment, choosenEquipment, onClick }) => {
  const index = choosenEquipment.findIndex((item) => item.inventory_number === equipment.inventory_number)
  const conteinerClassName = classNames(s.MarketplaceItem, index === -1 ? s.nonChoosenShadow : s.choosenShadow)

  return (
    <div className={conteinerClassName} onClick={() => onClick(equipment)}>
      <div className={s.imageWrapper}>
        <img src='https://www.gamersdecide.com/sites/default/files/team_fortress_2_best_heavy_minigun_main_image_.jpg' />
      </div>
      <div className={s.title}>
        {equipment.manufacturer} {equipment.model}
      </div>
      <div className={s.price}>{equipment.price_per_hour}</div>
      <div className={s.freePeaces}>{equipment.status}</div>
    </div>
  )
}

export default ChooseEquipment
