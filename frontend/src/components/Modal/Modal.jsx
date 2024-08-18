import { useEffect } from "react"
import ReactDOM from "react-dom"

import s from './Modal.module.css'


const Modal = ({ onClose, children, actionBar }) => {
  useEffect(()=>{
    document.body.classList.add('overflow-hidden')

    return () => {
      document.body.classList.remove('overflow-hidden')
    }

  }, [])


  return ReactDOM.createPortal(
    <div>
      <div
        onClick={onClose}
        className={s.container}
      ></div>
      <div className={s.whiteWindow}>
        <div className={s.wrapper}>
          {children}
          <div className={s.actionBar}>{actionBar}</div>
        </div>
      </div>
    </div>,
    document.querySelector(".modal-container")
  )
}

export default Modal
