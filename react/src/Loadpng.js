import React from 'react';
import axios from 'axios';
import picture from './requires.png'

class Loadpng extends React.Component {
    constructor(props) {
      super(props);
      // initializing states
      this.state = {
        isToggleOn: true,
        json: {},
        height: null,
        width: null
      };
  
      this.handle_get_png = this.get_png.bind(this);
      this.handleZoomIn = this.handleZoomIn.bind(this);
      this.handleZoomOut = this.handleZoomOut.bind(this);

      this.imgRef = React.createRef();
    }
  
    get_png(){
      this.setState({
        isToggleOn: false,
      });
      axios('/get_png',{
        method: "get",
        responseType: "blob",
      }).then(response => {
        console.log(response)
        let blob = new Blob([response.data], {type: "image/png"});
        let url = window.URL.createObjectURL(blob);
        this.setState({
            json: url
        });
      }).catch(err => {
        console.log(err);
      });
    }

    componentDidMount(){
      // Saving initial dimension of image as class properties
      this.initialHeight = this.imgRef.current.clientHeight;
      this.initialWidth = this.imgRef.current.clientWidth;
      console.log("height: %d width:%d ", this.initialHeight, this.initialWidth);
    }

    // Event handler callback for zoom in
    handleZoomIn(){
      // Fetching current height and width
      const height = this.imgRef.current.clientHeight;
      const width = this.imgRef.current.clientWidth;

      // Increase dimension(Zooming)
      this.setState({
        height : height + 10,
        width : width + 10,
      }) 
    }

    // Event handler callback zoom out
    handleZoomOut(){
      // Assigning original height and width
      this.setState({
        height : this.initialHeight,
        width : this.initialWidth,
      })
    }
  
    render() {
      const imgStyle = { height : this.state.height, width: this.state.width}
      return(
        <div>
            <h1>
            <button onClick={this.handle_get_png.bind(this, this.state.json)}>
            get_png
            </button>
          </h1>
        {/* Assign reference to DOM element     */}
        {/* <img style={imgStyle} ref={this.imgRef} src={this.state.json} alt='gfg' /> */}
        <img style={imgStyle} ref={this.imgRef} src={picture} alt='gfg' />
        <div>
          <button onClick={this.handleZoomIn}>Zoom In</button>
          <button onClick={this.handleZoomOut}>Zoom Out</button>
        </div>
        </div>
      )
    }
}

export default Loadpng;