import { useEffect, useState } from "react";
import { fetchProducts } from "../component/Products/service/product_serivice";

interface Image {
  image: string;
  alt_text: string;
}

export interface Product {
  id: number;
  name: string;
  images: Image[];
  category: {
    name: string;
  };
  shop: {
    name: string;
    province: string;
  };
  brand: {
    name: string;
  };
}
export const useProducts = () => {
  const [error, setErrors] = useState();
  const [products, setProducts] = useState<Product[]>([]);
  useEffect(() => {
    const { res, cancel } = fetchProducts();
    res
      .then((data) => {
        console.log(data);
        setProducts(data.data);
      })
      .catch((err) => {
        setErrors(err.response.data);
      });

    return () => cancel();
  }, []);
  return { products, error };
};
