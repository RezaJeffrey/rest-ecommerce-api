import { useProducts } from "../../hooks/useProducts";
import { SimpleGrid, Text } from "@chakra-ui/react";
import ProductCard from "./items/ProductCard";
import { productFilters } from "./service/product_serivice";

function ProductsMain(filters: productFilters) {
  const { products, error } = useProducts(filters);
  return (
    <>
      {error && <Text>{error}</Text>}
      <SimpleGrid columns={{ lg: 3, sm: 2, base: 1 }} spacing={10}>
        {products.map((product, index) => (
          <ProductCard result={product} key={index + 1} />
        ))}
      </SimpleGrid>
    </>
  );
}

export default ProductsMain;
