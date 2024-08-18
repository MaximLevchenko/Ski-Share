import g from '../../App.module.css'
import Header from '../../components/Header/Header'
import blackSnowFlake from '../../res/pics/blackSnowFlake.png'
import lightBlueSnowFlake from '../../res/pics/lightBlueSnowFlake.png'
import pinkSnowFlake from '../../res/pics/pinkSnowFlake.png'
import cyanSnowFlake from '../../res/pics/cyanSnowFlake.png'
import violetSnowFlake from '../../res/pics/violetSnowFlake.png'
import lowerWave from '../../res/pics/lowerWave.png'
import s from './PageWrapper.module.css'


const PageWrapper = ({ children }) => {
  return (
    <>
      <div className={s.PageWrapper}>
        <div className={g.container}>
          <Header />
          <img className={s.blackSnowFlake} src={blackSnowFlake} alt='SnowFlake' />
          <img className={s.lightBlueSnowFlake} src={lightBlueSnowFlake} alt='SnowFlake' />
          <img className={s.pinkSnowFlake} src={pinkSnowFlake} alt='SnowFlake' />
          <img className={s.lightBlueSnowFlakeSecond} src={lightBlueSnowFlake} alt='SnowFlake' />
          <img className={s.cyanSnowFlake} src={cyanSnowFlake} alt='SnowFlake' />
          <img className={s.violetSnowFlake} src={violetSnowFlake} alt='SnowFlake' />
          {children}
        </div>
      </div>
      <div className={s.lowerWave}>
        <img src={lowerWave} alt='Wave' />
      </div>
    </>
  )
}

export default PageWrapper
