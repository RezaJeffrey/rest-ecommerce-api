import Menu from "../Sidebar/items/Menu/Menu";
import { Checkbox, Flex, Stack } from "@chakra-ui/react";

interface Prob {
  id?: number;
  name: string;
  sku?: string;
  child: Prob[];
}

interface SecondProb extends Prob {
  handleCheck: (e: React.FocusEvent) => void;
}

function NestedList(prob: SecondProb) {
  return (
    <>
      {prob.child.length !== 0 ? (
        <Menu name={prob.name} key={prob.id}>
          {prob.child.map((obj) => (
            <NestedList
              child={obj.child}
              name={obj.name}
              id={obj.id}
              sku={obj.sku}
              handleCheck={prob.handleCheck}
            />
          ))}
        </Menu>
      ) : (
        <Stack spacing={1}>
          <Flex borderRadius="10px">
            <Checkbox
              size="md"
              border="10px"
              onFocus={() => console.log(prob.sku)}
              onChange={(e) => e.target.checked}
              key={prob.id}
            >
              {prob.name}
            </Checkbox>
          </Flex>
        </Stack>
      )}
    </>
  );
}

export default NestedList;
