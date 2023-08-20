import { useEffect } from "react";
import { fetchProducts } from "./service/product_serivice";

function ProductsMain() {
  useEffect(() => {
    const { res, cancel } = fetchProducts();
    res
      .then((data) => {
        console.log(data);
      })
      .catch((err) => {
        console.log(err);
      });
    // return () => cancel();
  }, []);
  return <div>ProductsMain</div>;
}

export default ProductsMain;
