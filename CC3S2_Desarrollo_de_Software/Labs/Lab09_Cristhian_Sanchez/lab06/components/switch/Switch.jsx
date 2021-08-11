import React, { useState } from "react";
import Example from "../example/Example";
import States from "../states/States";
import "./Switch.css";
function Switch(props) {
  const [name, setName] = useState("Example");
  const [button, setButton] = useState("Cambiar a State");
  const clickHandler = () => {
    if (name === "Example") {
      setName("States");
      setButton("Cambiar a Example");
    } else {
      setName("Example");
      setButton("Cambiar a State");
    }
  };
  return (
    <div className={name === "Example" ? "container" : "con"}>
      <div className="btn" onClick={clickHandler}>
        {button}
      </div>
      {name === "Example" ? <Example /> : <States />}
    </div>
  );
}

export default Switch;
