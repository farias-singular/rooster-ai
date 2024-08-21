```csharp
namespace Project.Application.Mappers
{
    public class BrandMapping : Profile
    {
        public BrandMapping()
        {
            CreateMap<Brand, CreateBrandDto>().ReverseMap();
        }
    }
}
```