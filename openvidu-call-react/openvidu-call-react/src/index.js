import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import VideoRoomComponent from "./components/VideoRoomComponent";
import registerServiceWorker from "./registerServiceWorker";
import MainComponent from "./components/MainComponent";

ReactDOM.render(
  // <VideoRoomComponent />, document.getElementById('root')
  <MainComponent />,
  document.getElementById("root")
);
registerServiceWorker();
