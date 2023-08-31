import { Stack } from "@chakra-ui/react";
import Categories from "./items/Categories/Categories";
import { categoryEventData } from "../NestedList/NestedList";

interface Prob {
  handleCategory: (e: categoryEventData) => void;
}

function Sidebar({handleCategory} : Prob) {
  return (
    <>
      <Stack padding={1}>
        <Categories handleCategory={(e) => handleCategory(e)}/>
      </Stack>
    </>
  );
}

export default Sidebar;
