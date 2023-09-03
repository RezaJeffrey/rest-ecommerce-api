import { useEffect, useState } from "react";
import { fetchSideBarItems } from "../component/Sidebar/service/sidebar-services";

export interface Category {
  id: number;
  name: string;
  image: string | null;
  sku: string;
  child: Category[];
}

export const useCategories = () => {
  const [error, setError] = useState<string>();
  const [categories, setCategories] = useState<Category[]>([]);
  useEffect(() => {
    const { res, cancel } = fetchSideBarItems<Category>(
      "/categories/api/v1/category/"
    );
    res
      .then((response) => {
        setError("");
        setCategories(response.data);
      })
      .catch((err) => {
        setError(err.response.data);
        setCategories([]);
      });
    return () => cancel();
  }, []);
  return { categories, error };
};
