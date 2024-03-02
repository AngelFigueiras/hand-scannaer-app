interface CategoryProps{
  params: {
    categories: string[],
    searchParams?: string
  }
}


export default function Category(props: CategoryProps){
  const { categories } = props.params

  
  return(
    <h1>Aqui van las categorias del sitio ecommerce: {categories}</h1>
  )
}