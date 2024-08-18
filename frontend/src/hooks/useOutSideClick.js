import { useEffect } from 'react'


export function useOutsideClick(ref, handleClick, ignoreClickOn) {
  useEffect(() => {
    function handleClickOutside(event) {
      if (ref.current && !ref.current.contains(event.target) && !ignoreClickOn?.current?.contains(event.target)) {
        handleClick()
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    document.addEventListener('touchend', handleClickOutside)

    return () => {
      document.removeEventListener('mousedown', handleClickOutside)
      document.removeEventListener('touchend', handleClickOutside)
    }
  }, [ref, handleClick, ignoreClickOn])
}
