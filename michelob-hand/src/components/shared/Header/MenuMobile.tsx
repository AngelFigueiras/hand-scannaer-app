//Metodo de next para reeedirigir la pagina sin recargar el sitio
import Link from "next/link";
import React from 'react';  

//Estilos
import styles from "./header.module.sass";
//import Image from "next/image";

interface MenuMobileProps {
  isMenuOpen: boolean;
  onToggleMenu: () => void;
}

export const MenuMobile: React.FC<MenuMobileProps> = ({
  isMenuOpen,
  onToggleMenu
}) =>{

  return(
      <div className={`${styles.menu_content_mobile} ${isMenuOpen ? styles.menu_mobile_open : ''}`}>

        <div className={styles.up_container}>

          <div className={styles.btn_open_menu_2}>
            <div className={styles.line1_2}></div>
            <div className={styles.line2_2}></div>
            <div className={styles.line3_2}></div>
          </div>

        </div>


        <div className={styles.list_container}>

          <ul className={styles.list_sections_mobile}>
            <Link className={styles.list_sections_a_mobile_2} href="/">
              <li>Home</li>
            </Link>
            <Link className={styles.list_sections_a_mobile_2} href="/handpromo">
              <li>Hand Scanner</li>
            </Link>
            <Link className={styles.list_sections_a_mobile_2} href="/store">
              <li>Store</li>
            </Link>
          </ul>

        </div>
      </div>
  )
}