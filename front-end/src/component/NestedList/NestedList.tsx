import { useState } from "react";
import Menu from "../Sidebar/items/Menu/Menu";
import { Checkbox, Flex, Stack } from "@chakra-ui/react";

export interface categoryEventData {
  sku: string;
  isChecked: boolean;
}

interface Prob {
  id?: number;
  name: string;
  sku?: string;
  child: Prob[];
}

interface SecondProb extends Prob {
  handleCheck: (e: categoryEventData) => void;
  isChecked: boolean;
}

function NestedList({id, name, sku = "", child, handleCheck, isChecked}: SecondProb) {
  const [isToggled, setIsToggled] = useState(false);
  return (
    <>
      {child.length !== 0 ? (
        <Stack padding={5}>
          <Menu name={name} key={id}>
            {child.map((obj) => (
              <NestedList
                key={obj.id}
                child={obj.child}
                name={obj.name}
                id={obj.id}
                sku={obj.sku}
                isChecked={isChecked}
                handleCheck={handleCheck}
              />
            ))}
          </Menu>
        </Stack>
      ) : (
        <Stack spacing={1}>
          <Flex borderRadius="10px">
            <Checkbox
              size="md"
              border="10px"
              isChecked={isToggled}
              onChange={() => {
                setIsToggled(!isToggled);
                handleCheck(
                  isChecked
                    ? {
                        sku: sku,
                        isChecked: isToggled,
                      }
                    : {
                        sku: sku,
                        isChecked: !isToggled,
                      }
                );
              }}
              key={id}
            >
              {name}
            </Checkbox>
          </Flex>
        </Stack>
      )}
    </>
  );
}

export default NestedList;
