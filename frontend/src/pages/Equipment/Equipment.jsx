import { uniq } from 'lodash'

import g from '../../App.module.css'
import SkeletonBlocks from '../../components/Loaders/SkeletonBlocks'
import MarketplaceItem from '../../components/MarketplaceItem/MarketplaceItem'
import { useFetchEquipmentsQuery } from '../../store/apiSlices/equipmentApiSlice'
import s from './Equipment.module.css'


const Equipment = () => {
  const { data, error, isFetching } = useFetchEquipmentsQuery()

  let content
  let brands
  let categories
  let renderedBrands
  let renderedCategories

  if (isFetching) {
    content = <SkeletonBlocks />
  } else if (error) {
    content = <div>Error loading items</div>
  } else {
    content = data.map((item) => <MarketplaceItem key={item.inventory_number} item={item} />)
    brands = uniq(data.map((item) => item.manufacturer))
    categories = uniq(data.map((item) => item.category))

    renderedBrands = brands.map((brand) => (
      <label className={s.checkBoxContainer} key={brand}>
        <input type='checkbox' />
        <span className={s.checkmark}></span>
        {brand}
      </label>
    ))
    renderedCategories = categories.map((category) => (
      <label className={s.checkBoxContainer} key={category}>
        <input type='checkbox' />
        <span className={s.checkmark}></span>
        {category}
      </label>
    ))
  }

  return (
    <div className={g.initialPageContainer}>
      <div className={g.title}>Equipment</div>
      <div className={s.marketplaceWrapper}>
        <div className={s.filterColumn}>
          <div className={s.filterTitle}>Filter</div>
          <div className={s.filterBlock}>
            <div className={s.filterPanelTitle}>Price</div>
            <div className={s.filterInputWrapper}>
              <div className={s.filterInput}>
                <input type='text' />
              </div>
              <div className={s.filterTab}>&#8211;</div>
              <div className={s.filterInput}>
                <input type='text' />
              </div>
            </div>
          </div>
          <div className={s.filterBlock}>
            <div className={s.filterPanelTitle}>Brands</div>
            {renderedBrands}
          </div>
          <div className={s.filterBlock}>
            <div className={s.filterPanelTitle}>Equipment</div>
            {renderedCategories}
          </div>
        </div>
        <div className={s.marketColumn}>{content}</div>
      </div>
    </div>
  )
}

export default Equipment
