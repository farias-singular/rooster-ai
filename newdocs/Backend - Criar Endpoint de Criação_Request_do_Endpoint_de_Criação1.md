```csharp
namespace Project.API.Controllers.Organizations.APIs.Brands.Endpoints.CreateBrand
{
    public class CreateBrandRequest
    {
        public string Id { get; set; }
        public Guid CategoryId { get; set; }
        public string Name { get; set; }
        public string? Title { get; set; }
    }
}
```