export class NotNormalButton extends Element {
    
    
    componentDidMount() {
        var btn_name = this.attributes["btn_name"] || "button";
        this.content([<button>{btn_name}</button>]);
      }  
}