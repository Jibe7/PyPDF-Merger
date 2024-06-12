export class Hello extends Element 
{
  componentDidMount() {
    var message = this.attributes["message"] || "?";
    this.content(<h1>{message}</h1>);
  }
}