import { useCategories } from "../../../../hooks/useCategories";
import { Text } from "@chakra-ui/react";
import NestedList, { categoryEventData } from "../../../NestedList/NestedList";

interface Prob {
  handleCategory: (e: categoryEventData) => void;
}

function Categories({handleCategory} : Prob) {
  const { categories, error } = useCategories();

  const handleChange = (e: categoryEventData) => {
    handleCategory(e);
  };

  return (
    <>
      {error && <Text>{error}</Text>}
      {categories.length === 0 ? (
        <Text>couldn't find any categories!</Text>
      ) : (
        <NestedList
          child={categories}
          isChecked={false}
          name="categories"
          handleCheck={(e) => handleChange(e)}
        />
      )}
    </>
  );
}

export default Categories;
