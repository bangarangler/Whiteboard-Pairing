class Stack {
  constructor() {
    this.storage = [];
  }

  push(item) {
    this.storage.push(item);
  }

  pop() {
    return this.storage.pop();
  }

  peek() {
    return this.storage[this.storage.length - 1];
  }

  isEmpty() {
    return this.storage.length === 0;
  }

  printContents() {
    this.storage.forEach(elem => console.log(elem));
  }
}

const sortStack = stack => {
  //console.log(stack.printContents());
  //HOLDING STACK
  let isNotFinished = true;
  const tempStack = new Stack();
  while (isNotFinished) {
    //BOX CHECKER
    let tempValue = stack.pop();
    // LOOP THROUGH STACK
    for (let i = stack.storage.length; i >= 0; i--) {
      console.log("current stackPeek: ", stack.peek(), tempValue);
      // CHECK IF VALUE IN BOX IS > VALUE IN BOX CHECKER
      if (stack.isEmpty() === 0) {
        tempStack.push(tempValue);
        tempValue = null;
        break;
      } else if (tempValue <= stack.peek()) {
        // PUSH THAT VALUE TO TEMP STACK
        tempStack.push(stack.pop());
        // IF STACK IS EMPTY PUSH TEMPSTACK BACK TO STACK
      } else {
        // IF IT'S NOT > VALUE IN THE BOX IT BECOMES NEW BOX
        tempStack.push(tempValue);
        tempValue = stack.pop();
        console.log("new temp value: ", tempValue);
      }
      console.log("tempStack: ", tempStack);
    }
    isNotFinished = false;
    for (let i = tempStack.storage.length - 1; i >= 0; i--) {
      stack.push(tempStack.pop());
      if (tempStack.storage.length > 0) {
        if (stack.peek() > tempStack.peek()) {
          isNotFinished = true;
        }
      }
    }
    console.log(stack.storage);
  }
  return stack.storage;
};

const JStack = new Stack();
JStack.push(4);
JStack.push(10);
JStack.push(8);
JStack.push(5);
JStack.push(1);
JStack.push(6);

//JStack.printContents();
console.log(sortStack(JStack));
