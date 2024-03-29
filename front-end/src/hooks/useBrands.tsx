import { useEffect, useState } from "react";
import { fetchSideBarItems } from "../component/Sidebar/service/sidebar-services";

export interface Brand {
  id: number;
  sku: string;
  name: string;
  image: string | null;
}

export const useBrands = () => {
  const [error, setError] = useState<string>();
  const [brands, setBrands] = useState<Brand[]>();
  useEffect(() => {
    const { res, cancel } = fetchSideBarItems<Brand>("/brands/api/v1/brand/");
    res
      .then((response) => {
        setError("");
        setBrands(response.data);
      })
      .catch((err) => {
        if (err.response) {
          setError(err.response.data);
          setBrands([]);
        }
      });
    return () => cancel();
  }, []);
  return { brands, error };
};
