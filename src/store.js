/*
 * @Description: 
 * @Author: 
 * @Date: 2023-06-21 19:10:15
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2023-08-17 23:12:54
 */
// store.js
import { ref, reactive } from 'vue'
import { createGlobalState, rand } from '@vueuse/core'
import dayjs from 'dayjs';

export const useGlobalState = createGlobalState(
  () => {
    const isEase = ref(false);
    const events = reactive([])
    let cnt = 0
    setInterval(() => {
      const device = rand(1, 4)
      let port = -1
      if (device === 1) {
        port = rand(0, 4)
      }
      else if (device === 4) {
        port = rand(0, 3)
      }
      else {
        port = rand(0, 1)
      }
      events.push({
        id: cnt++,
        device: `S${device}`,
        // port: `eth${port}`,
        rate: `${rand(753, 958)/1000}`,
        duration: `${rand(15, 51)/10}h`,
        date: dayjs().format('YYYY.MM.DD.HH')
      })
    }, 1000);
    return { isEase, events }
  }
)