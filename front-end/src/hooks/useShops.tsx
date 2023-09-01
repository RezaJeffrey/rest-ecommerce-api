import { useEffect, useState } from "react";
import { fetchSideBarItems } from "../component/Sidebar/service/sidebar-services";

interface Shop {
  id: number;
  name: string;
  province: string;
  sku: string;
}

export const useShop = () => {
  const [errorMessage, setErrorMessage] = useState<string>();
  const [shops, setShops] = useState<Shop[]>([]);
  useEffect(() => {
    const { res, cancel } = fetchSideBarItems<Shop>("/shops/api/v1/shop/");
    res
      .then((response) => {
        setErrorMessage("");
        setShops(response.data);
      })
      .catch((err) => {
        setErrorMessage(err.message);
        setShops([]);
      });
    return () => cancel();
  }, []);
  return { shops, errorMessage };
};
