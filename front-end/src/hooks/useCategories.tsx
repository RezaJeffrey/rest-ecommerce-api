import { useEffect, useState } from "react";
import { fetchCategories } from "../component/Sidebar/service/sidebar-services";

export interface Category {
  id: number;
  name: string;
  image: string | null;
  sku: string;
  child: Category[];
}

export const useCategories = () => {
  const [error, setError] = useState();
  const [categories, setCategories] = useState<Category[]>([]);
  useEffect(() => {
    const { res, cancel } = fetchCategories();
    res
      .then((response) => {
        setCategories(response.data);
      })
      .catch((err) => {
        setError(err.response.data);
      });
    return () => cancel();
  }, []);
  return { categories, error };
};
