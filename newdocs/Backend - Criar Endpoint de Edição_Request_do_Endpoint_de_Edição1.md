```csharp
namespace Project.API.Controllers.Organizations.APIs.Brands.Endpoints.UpdateBrand
{
    public class UpdateBrandRequest
    {
        public Guid CategoryId { get; set; }
        public string Name { get; set; }
        public string? Title { get; set; }
    }
}
```