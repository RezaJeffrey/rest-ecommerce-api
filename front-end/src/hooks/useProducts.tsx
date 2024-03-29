import { useEffect, useState } from "react";
import {
  fetchProducts,
  productFilters,
} from "../component/Products/service/product_serivice";

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
export const useProducts = (filter: productFilters, deps?: any[]) => {
  const [error, setErrors] = useState();
  const [products, setProducts] = useState<Product[]>([]);
  useEffect(
    () => {
      const { res, cancel } = fetchProducts(filter);
      res
        .then((data) => {
          setProducts(data.data);
        })
        .catch((err) => {
          if (err.response) {
            console.log(err.response.data);
            setErrors(err.response.data);
          }
        });
      return () => cancel();
    },
    deps ? [...deps] : [filter]
  );
  return { products, error };
};
