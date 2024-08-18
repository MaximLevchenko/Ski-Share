import s from './MarketplaceItem.module.css'


const MarketplaceItem = ({ item }) => {
  return (
    <div className={s.MarketplaceItem}>
      <div className={s.imageWrapper}>
        <img src='https://www.gamersdecide.com/sites/default/files/team_fortress_2_best_heavy_minigun_main_image_.jpg' />
      </div>
      <div className={s.title}>{item.model}</div>
      <div className={s.price}>{item.price_per_hour}</div>
      <div className={s.freePeaces}>{item.status}</div>
    </div>
  )
}

export default MarketplaceItem
