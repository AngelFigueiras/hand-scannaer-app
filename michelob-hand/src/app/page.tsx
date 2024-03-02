import { Description } from "../components/home/Description"
import { Hero } from "../components/home/Hero/Hero";


export default function Home() {
  console.log('Hola mundo')

  return (
    <main>
      <Hero></Hero>
      <Description></Description>
    </main>
  );
}
