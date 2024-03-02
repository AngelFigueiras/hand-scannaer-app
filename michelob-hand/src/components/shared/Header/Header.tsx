//Metodo de next para reeedirigir la pagina sin recargar el sitio
import Link from "next/link";
import Image from "next/image";
import React, {useState} from "react";

//Estilos
import styles from "./header.module.sass";



//componentes
import { MenuMobile } from "./MenuMobile";



export const Header = () =>{
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return(
    <header className={styles.Header}>
      <nav className={styles.navbar_content}>

        <div className={styles.logo_desktop}>
          <Image src="/images/logo.svg"
            className={styles.logo}
            alt="logo michelob"
            width={200}
            height={30}
          />
        </div>

        <ul className={styles.list_sections}>
          <Link className={styles.list_sections_a} href="/">
            <li>Home</li>
          </Link>
          <Link className={styles.list_sections_a} href="/handpromo">
            <li>Hand Scanner</li>
          </Link>
          <Link className={styles.list_sections_a} href="/store">
            <li>Store</li>
          </Link>
        </ul>

        <MenuMobile isMenuOpen={isMenuOpen} onToggleMenu={()=>setIsMenuOpen(!isMenuOpen)} />

        <div className={styles.btn_open_menu}
          onClick={() => setIsMenuOpen(!isMenuOpen)}
        >
          <div className={styles.line1}></div>
          <div className={styles.line2}></div>
          <div className={styles.line3}></div>
        </div>

      </nav>
    </header>
  )
}
