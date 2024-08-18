import classNames from 'classnames'
import { AiOutlineHome, AiOutlinePlus, AiOutlineTool, AiOutlineUser } from 'react-icons/ai'
import { FiLogOut, FiUsers } from 'react-icons/fi'
import { RiUserSettingsLine } from 'react-icons/ri'
import { useDispatch } from 'react-redux'
import { Link, useLocation } from 'react-router-dom'

import logo from '../../res/pics/logo.svg'
import { logout } from '../../store/slices/authSlice'
import Dropdown from '../Dropdown/Dropdown'
import s from './Header.module.css'


const navigation = [
  {
    link: '/equipment',
    icon: <AiOutlineHome size={30} alt='Equipment' />,
  },
  {
    link: '/profile',
    icon: <AiOutlineUser size={30} alt='Profile' />,
  },
  {
    link: '/clients',
    icon: <FiUsers size={30} alt='Clients' />,
  },
  {
    link: '/employees',
    icon: <RiUserSettingsLine size={30} alt='Employees' />,
  },
  {
    link: '/rents',
    icon: <AiOutlineTool size={30} alt='Rents' />,
  },
]

const dropdownMenu = [
  {
    title: 'New rent',
    navigate: '/new-rent',
  },
  {
    title: 'New client',
    navigate: '/new-client',
  },
  {
    title: 'New equipment',
    navigate: '/new-equipment',
  },
]

const Header = () => {
  const dispatch = useDispatch()

  const path = '/' + useLocation().pathname.split('/')[1]

  const checkActiveLink = (link) => {
    if (link === path) {
      return true
    }

    return false
  }

  const handleLogout = () => {
    dispatch(logout())
  }

  const renderedLinks = navigation.map((nav, index) => {
    const className = classNames(s.iconLink, checkActiveLink(nav.link) && s.activeLink)

    return (
      <div key={index} className={className}>
        <Link to={nav.link}>{nav.icon}</Link>
      </div>
    )
  })
  renderedLinks.push()

  return (
    <div className={s.Header}>
      <div className={s.headerContainer}>
        <div className={s.iconColumn}>
          {renderedLinks}
          <div className={s.iconLink}>
            <FiLogOut size={30} alt='Logout' onClick={handleLogout} />
          </div>
        </div>
        <div className={s.actionColumn}>
          <div className={s.buttonWrapper}>
            <Dropdown dropdownMenu={dropdownMenu}>
              Create <AiOutlinePlus alt='plus' size={37} />
            </Dropdown>
          </div>
          <div className={s.logoWrapper}>
            <img src={logo} alt='logo' />
          </div>
        </div>
      </div>
    </div>
  )
}

export default Header
