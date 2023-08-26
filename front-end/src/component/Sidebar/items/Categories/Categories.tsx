import { useCategories } from "../../../../hooks/useCategories";
import { Text } from "@chakra-ui/react";
import NestedList from "../../../NestedList/NestedList";

function Categories() {
  const { categories, error } = useCategories();
  console.log(categories);
  return (
    <>
      {error && <Text>{error}</Text>}
      {categories.length === 0 ? <Text>couldn't find any categories!</Text> :
      <NestedList
        child={categories}
        name="categories"
        handleCheck={(e) => console.log(e)}
      />
  }
    </>
  );
}

export default Categories;
