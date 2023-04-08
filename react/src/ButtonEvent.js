import React from 'react';
import axios from 'axios';

class ButtonEvent extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        isToggleOn: true,
        str: 'str test'
      };
  
      this.handleClick = this.Click.bind(this);
    }
  
    Click(){
      this.setState({
        isToggleOn: false,
      });
      const data = {string: this.state.str}
      console.log(data);
      axios.post('/str_test', data).then(response => {
        console.log(response.data);
        this.setState({
            str: response.data['string']
        });
      }).catch(err => {
        console.log(err);
      });
      this.setState({
        isToggleOn: true,
      });
    }
  
    render() {
      return(
        <div>
          <h1>
          <button disabled={!this.state.isToggleOn} onClick={this.handleClick.bind(this, this.state.str)}>
            get_info
          </button>
          </h1>
          <h1>{this.state.str}</h1>
        </div>
      )
    }
}

export default ButtonEvent;