
'use client'

import { Inter } from "next/font/google";

//Componentes compartidos
import { Header } from "../components/shared/Header";
import { Footer } from "../components/shared/Footer";
import "../sass/globals.sass";

const inter = Inter({ subsets: ["latin"] });



export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {

  return (
    <html lang="en">


      <body className={inter.className}>

        <Header></Header>

        {children}

        <Footer></Footer>

      </body>


    </html>
  );
}
