import React, { Component } from "react";
import ReactDOM from "react-dom";
import { render } from "react-dom";
import VideoRoomComponent from "./VideoRoomComponent";

class MainComponent extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isRendered: true,
    };
  }

  handleClick = () => {
    // 버튼을 클릭할 때마다 isRendered 상태를 반전시킵니다.
    this.setState((prevState) => ({
      isRendered: !prevState.isRendered,
    }));
  };

  render() {
    return (
      <div>
        {!this.state.isRendered && <VideoRoomComponent></VideoRoomComponent>}
        <button onClick={this.handleClick}></button>
      </div>
    );
  }
}

export default MainComponent;
