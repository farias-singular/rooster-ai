```csharp
namespace Project.Domain.Brands
{
    public interface IBrandRepository
    {
        Task<Brand> CreateAsync(Brand entity);

        Task<PaginatedResponse<Brand>> GetAllAsync(
            Specification<Brand>? specification = null, 
            OrderStrategy<Brand>? strategy = null,
            int? skip = null, 
            int? take = null);

        Task<Brand?> GetByIdAsync(string id);

        Brand Update(Brand entity);

        Brand Delete(Brand entity);
    }
}
```