import React from 'react';

class Clock extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        datetime: new Date(),
        isToggleOn: true,
        str: 'aaaa'
      };
  
      this.handleClick = this.Click.bind(this);
    }
  
    tick() {
      this.setState({
        datetime : new Date()
      });
    }
  
    Click(time){
      this.tick()
      this.setState({
        isToggleOn: !this.state.isToggleOn,
        str: time.toLocaleTimeString()
      });
    }
  
    render() {
      return(
        <div>
          <h1>{this.props.name}
          <button onClick={this.handleClick.bind(this, this.state.datetime)}>
            {this.state.isToggleOn ? 'update':'close'}
          </button></h1>
          <h1>{this.state.str}</h1>
        </div>
      )
    }
}

Clock.defaultProps = {
name : 'date'
};

export default Clock;