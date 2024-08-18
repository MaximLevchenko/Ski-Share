import { useCallback } from "react"


const getDayNumber = (m, y) => {
    if (m === 1 || m === 3 || m === 5 || m === 7 || m === 8 || m === 10 || m === 12) {
        return 31
    } else if (m === 4 || m === 6 || m === 5 || m === 9 || m === 11) {
        return 30
    } else {
        if ((y % 4 === 0 && y % 100 !== 0) || (y % 100 === 0 && y % 400 === 0)) {
            return 29
        } else {
            return 28
        }
    }
}

export const useDate = () => {
    const getMonthArr = useCallback((date) => {
        let resultArr = []
        let dayCount = getDayNumber(date.getMonth() + 1, date.getFullYear())
        const dateFirst = new Date(date.getFullYear(), date.getMonth(), 1)
        const firstDay = dateFirst.getDay()
        let emptyCountStart
        if (firstDay === 0) {
            emptyCountStart = 6
        } else {
            emptyCountStart = firstDay - 1
        }
        for (let i = 0; i < emptyCountStart; i++) {
            resultArr.push({
                m: date.getMonth() + 1,
                y: date.getFullYear(),
                d: 0
            })
        }
        for (let i = 1; i <= dayCount; i++) {
            resultArr.push({
                m: date.getMonth() + 1,
                y: date.getFullYear(),
                d: i
            })
        }
        while (resultArr.length < 42) resultArr.push({
            m: date.getMonth() + 1,
            y: date.getFullYear(),
            d: 0
        })
        let res = []
        while (resultArr.length) res.push(resultArr.splice(0, 7));
        return res
    })

    return {getMonthArr}
}