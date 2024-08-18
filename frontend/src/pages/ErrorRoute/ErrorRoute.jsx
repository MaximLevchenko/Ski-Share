import logo from '../../res/pics/logo.svg'
import s from './ErrorRoute.module.css'
import g from '../../App.module.css'


const ErrorRoute = () => {
  return (
    <div className={s.ErrorRoute}>
      <div className={g.title}>This URL does not exits</div>
      <div><img src={logo}/></div>
    </div>
  )
}

export default ErrorRoute