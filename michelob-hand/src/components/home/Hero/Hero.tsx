'use client'

import styles from "./hero.module.sass"
// Import Swiper React components
import { Swiper, SwiperSlide } from 'swiper/react';

import { Pagination } from "swiper/modules";

// Import Swiper styles
import 'swiper/css';

export const Hero = ({
  Pagination = { clickable: true },
}) => {
  return(
    <section className={styles.Hero}>

      <Swiper
        spaceBetween={50}
        slidesPerView={3}
        onSlideChange={() => console.log('slide change')}
        onSwiper={(swiper) => console.log(swiper)}
        pagination = { Pagination }
      >
        <SwiperSlide>Slide 1</SwiperSlide>
        <SwiperSlide>Slide 2</SwiperSlide>
        <SwiperSlide>Slide 3</SwiperSlide>
        <SwiperSlide>Slide 4</SwiperSlide>
      </Swiper>
      
    </section>
  )
}