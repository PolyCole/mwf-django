import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("api/bulletinpost")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
      <div class="list-group">
        {this.state.data.map(post => {
          return (
          <div class="list-group-item" id={post.id}>
            <div className="d-flex w-100 justify-content-between">
                  <h5 className="mb-1">{post.user}</h5>
                  <small>{post.created_at}</small>
            </div>
            <p className="mb-1">{post.message}</p>
          </div>
          );
        })}
      </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);