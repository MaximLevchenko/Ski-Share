import { AiOutlineMail, AiOutlinePhone, AiOutlineUser } from 'react-icons/ai'
import { useSelector } from 'react-redux'

import g from '../../App.module.css'
import snow from '../../res/pics/snow.png'
import { selectActualUser } from '../../store/slices/authSlice'
import s from './Profile.module.css'


const Profile = () => {
  const user = useSelector(selectActualUser)
  const employeName = `${user.employeeName} ${user.employeeSurname}`

  const profileInfo = [
    {
      icon: <AiOutlinePhone alt='Phone number' size={25} />,
      data: user.employeePhone,
    },
    {
      icon: <AiOutlineMail alt='Mail' size={25} />,
      data: user.employeeEmail,
    },
    { icon: <AiOutlineUser alt='Work as' size={25} />, data: user.employeePosition },
  ]

  const renderedProfileInfo = profileInfo.map((info) => (
    <div className={s.profileRow} key={info.data}>
      <div>{info.icon}</div>
      <div className={s.data}>{info.data}</div>
    </div>
  ))

  const stats = [
    'Working time - 8 h. 35 min.',
    'Number of rents - 0',
    'Number of сustomers - 0',
    'Rental income - 0',
    'Expenses - 0',
  ]

  const renderedStats = stats.map((stat) => (
    <div className={s.stat} key={stat}>
      {stat}
    </div>
  ))

  return (
    <div className={g.initialPageContainer}>
      <div className={g.title}>Profile</div>
      <div className={s.profileWrapper}>
        <div className={s.profileInfo}>
          <div className={s.profilePhoto}>
            <img src='https://i1.sndcdn.com/avatars-1izkebM3cqeF0hcO-uo8bjQ-t500x500.jpg' alt='Profile' />
          </div>
          <div className={s.profileData}>
            <div className={s.name}>{employeName}</div>
            {renderedProfileInfo}
          </div>
        </div>
        <div className={s.profileStats}>
          <div className={s.statsContainer}>
            <div className={s.snow}>
              <img src={snow} alt='Snow' />
            </div>
            <div className={s.statsTitle}>Today's shift</div>
            <div className={s.statsBlock}>{renderedStats}</div>
          </div>
        </div>
      </div>
      <div className={s.rentWrapper}>
        <div className={g.subtitle}>Rent history</div>
        {/* <Table /> */}
      </div>
    </div>
  )
}

export default Profile
